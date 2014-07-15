import datetime


def howLongAgo(ts):
    now = datetime.datetime.utcnow()
    seconds = (now - ts).total_seconds()
    if seconds < 3:
        return "just now"
    elif seconds < 60:
        return "%d seconds ago" % int(round(seconds))
    elif seconds < 3600:
        numMinutes = seconds / 60.0
        if int(round(numMinutes)) > 1:
            return "%d minutes ago" % int(round(numMinutes))
        else:
            return "1 minute ago"
    elif seconds < 3600 * 24:
        numHours = seconds / 3600.0
        if int(round(numHours)) > 1:
            return "%d hours ago" % int(round(numHours))
        else:
            return "1 hour ago"
    else:
        numDays = seconds / (24 * 3600.0)
        if int(round(numDays)) > 1:
            return "%d days ago" % int(round(numDays))
        else:
            return "1 day ago"
