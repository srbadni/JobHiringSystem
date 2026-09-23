class LocalStorageService {
    constructor(private readonly prefix = "app") {}

    private get storage(): Storage | null {
        if (typeof window === "undefined") {
            return null;
        }

        return window.localStorage;
    }

    private createKey(key: string): string {
        return `${this.prefix}:${key}`;
    }

    set<T>(key: string, value: T): boolean {
        try {
            this.storage?.setItem(
                this.createKey(key),
                JSON.stringify(value),
            );

            return this.storage !== null;
        } catch {
            return false;
        }
    }

    get<T>(key: string): T | null {
        try {
            const value = this.storage?.getItem(this.createKey(key));

            if (value === null || value === undefined) {
                return null;
            }

            return JSON.parse(value) as T;
        } catch {
            return null;
        }
    }

    remove(key: string): void {
        this.storage?.removeItem(this.createKey(key));
    }

    has(key: string): boolean {
        return this.storage?.getItem(this.createKey(key)) !== null;
    }

    clear(): void {
        const storage = this.storage;

        if (!storage) return;

        const prefix = `${this.prefix}:`;

        for (let index = storage.length - 1; index >= 0; index--) {
            const key = storage.key(index);

            if (key?.startsWith(prefix)) {
                storage.removeItem(key);
            }
        }
    }
}

export const localStorageService = new LocalStorageService("job-hiring");
