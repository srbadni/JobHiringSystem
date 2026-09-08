const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";

export async function get<T>(path: string, init?: RequestInit): Promise<T> {
    const response = await fetch(`${apiUrl}${path}`, init);
    if (!response.ok) throw new Error(`API request failed with status ${response.status}`);
    return response.json() as Promise<T>;
}
