export interface PaginatedResponse<T> {
    items: T[];
    total: number;
    page_index: number;
    page_size: number;
}

export interface Pagination {
    total: number;
    page_index: number;
    page_size: number;
}
