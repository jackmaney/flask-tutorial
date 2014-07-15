import datetime


def howLongAgo(ts):
    now = datetime.datetime.utcnow()
    seconds = (now - ts).total_seconds()
    print seconds
    if seconds < 1:
        return "just now"
    elif seconds < 60:
        return "%d seconds ago" % int(round(seconds))
    elif seconds < 3600:
        numMinutes = seconds / 60.0
        return "%d minutes ago" % int(round(numMinutes))
    elif seconds < 3600 * 24:
        numHours = seconds / 3600.0
        return "%d hours ago" % int(round(numHours))
    else:
        numDays = seconds / (24 * 3600.0)
        return "%d days ago" % int(round(numDays))
