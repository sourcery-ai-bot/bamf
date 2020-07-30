from huey.contrib.djhuey import task

from .utils.comicimporter import ComicImporter


@task()
def import_comic_files_task():
    ci = ComicImporter()
    ci.import_comic_files()

    return


@task()
def refresh_issue_task(cvid):
    ci = ComicImporter()
    return ci.refreshIssueData(cvid)


@task()
def refresh_series_task(cvid):
    ci = ComicImporter()
    return ci.refreshSeriesData(cvid)


@task()
def refresh_publisher_task(cvid):
    ci = ComicImporter()
    return ci.refreshPublisherData(cvid)


@task()
def refresh_character_task(cvid):
    ci = ComicImporter()
    return ci.refreshCharacterData(cvid)


@task()
def refresh_creator_task(cvid):
    ci = ComicImporter()
    return ci.refreshCreatorData(cvid)


@task()
def refresh_team_task(cvid):
    ci = ComicImporter()
    return ci.refreshTeamData(cvid)


@task()
def refresh_arc_task(cvid):
    ci = ComicImporter()
    return ci.refreshArcData(cvid)
