export function timeAgo(dateString: string): string {
    const date = new Date(dateString);
    const now = new Date();

    const diffMs = now.getTime() - date.getTime();

    const seconds = Math.floor(diffMs / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (days > 0) {
        const remainingHours = hours % 24;

        if (remainingHours > 0) {
            return `${days} روز و ${remainingHours} ساعت قبل`;
        }

        return `${days} روز قبل`;
    }

    if (hours > 0) {
        return `${hours} ساعت قبل`;
    }

    if (minutes > 0) {
        return `${minutes} دقیقه قبل`;
    }

    return "همین الان";
}
