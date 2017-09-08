export interface Comic {
    pk: number,
    external_id: number,
    title: string,
    cover_url: string,
    tracked_by: string[],
    is_tracked: boolean
}
