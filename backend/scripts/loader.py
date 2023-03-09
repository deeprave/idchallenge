#!/usr/bin/env python
import csv
import sys
import logging
from pathlib import Path
from http import HTTPStatus

import django
import urlpath
import cmdline
from django_settings_env import Env

env = Env(readenv=True, parents=True)


CHUNK_SIZE = 65536
LOG_FORMAT = '%(asctime)s %(message)s'


def init(settings_str: str = None):
    """
    initialise django, so we can use the Django settings and ORM
    :param settings_str: settings module path (optional)
    """
    if settings_str is not None:
        env.setdefault('DJANGO_SETTINGS_MODULE', settings_str)
    cmdline.add_pythonpath(Path.cwd())
    django.setup()
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def fatal(message: str, code: int = 1):
    logging.critical(message)
    sys.exit(code)


def download_file(url: urlpath.URL, dest_path: Path):
    logging.info(f"Downloading {download_url}")
    logging.info(f"         => {dest_path}")

    response = url.get(stream=True)
    if response.status_code != HTTPStatus.OK:
        fatal(f"Download failed, http status = {response.status_code}")
    bytes_written = 0
    with dest_path.open("wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            bytes_written += len(chunk)
            f.write(chunk)
    logging.info(f"Succeeded: {download_url.name}, size={bytes_written}")
    return dest_path


def ingest_csv(source: Path) -> int:
    from api.models import (
        Gender,
        Age,
        State,
        RegionType,
        Region,
        Year,
        Statistic
    )

    # ensure statistics table is cleared
    Statistic.objects.all().delete()

    gender, age, state, regiontype, region, year = None, None, None, None, None, None

    def ingest_row(row: [str]):
        """
        ingest a row read from the CSV
        This is not a particularly performant approach as fields are being
        fully normalised, which may not be necessary.
        get_or_create is only avoided if the previous record still applies.
        Possible improvements:
            - cache values or smaller normalised values to reduce get_or_create overhead
            - use something like the Oracle SQL Loader (for target db) rather than python
        :param row:
        :return:
        """
        nonlocal gender, age, state, regiontype, region, year

        for col in range(0, len(row), 2):
            match col:

                case 0:  # gender_id, gender_desc
                    record_id = int(row[0])
                    if gender is None or record_id != gender.id:
                        gender, _ = Gender.objects.get_or_create(id=record_id, gender=row[1])

                case 2:  # age, age_desc
                    try:
                        record_id = int(row[2])
                    except ValueError:
                        record_id = -1
                    if age is None or age.id != record_id:
                        age, _ = Age.objects.get_or_create(id=record_id, age=row[3])

                case 4:  # id, state
                    record_id = int(row[4])
                    if state is None or state.id != record_id:
                        state, _ = State.objects.get_or_create(id=record_id, state=row[5])

                case 6:
                    code = row[6]
                    if regiontype is None or regiontype.id != code:
                        regiontype, _ = RegionType.objects.get_or_create(id=code, geography_level=row[7])

                case 8:
                    asgs = int(row[8])
                    if region is None or region.id != asgs:
                        region, _ = Region.objects.get_or_create(id=asgs, region=row[9])

                case 10:
                    record_id = int(row[10])
                    if year is None or year.id != record_id:
                        year, _ = Year.objects.get_or_create(id=record_id, year=row[11])

                case 12:
                    Statistic.objects.create(
                        gender=gender,
                        age=age,
                        state=state,
                        regiontype=regiontype,
                        region=region,
                        year=year,
                        value=int(row[12]),
                        flag_codes=row[13],
                        flags=row[14]
                    )

    headers = None
    count = 0
    with source.open(newline='', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel')
        for rw in csvreader:
            if headers is None:
                headers = rw
            else:
                ingest_row(rw)
                count += 1
    return count


if __name__ == '__main__':
    init("config.settings")

    from django.conf import settings
    download_dir = settings.DOWNLOAD_PATH
    download_dir.mkdir(0x777, parents=True, exist_ok=True)
    download_url = urlpath.URL(settings.DOWNLOAD_URL)

    dest = download_file(download_url, download_dir / download_url.name)

    rows = ingest_csv(dest)

    logging.info(f"{rows} rows ingested.")
