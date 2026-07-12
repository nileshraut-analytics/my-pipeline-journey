## [Unreleased] - 2026-07-12

### Fixed
- Removed redundant `.count()` calls in `validate_data()` and `aggregate_data()` that were triggering repeated full scans of the DataFrame — each row count is now computed once, stored in a variable, and reused across both the print and log statements.
- Fixed broken data flow between `validate_data()`, `aggregate_data()`, and `data_quality_report()` after adding count tracking — updated function signatures, return statements, and call-site unpacking so counts pass correctly through the pipeline instead of raising unpacking/type errors.

### Changed
- `validate_data()` now returns `(clean_rows, bad_rows, clean_rows_count, bad_rows_count)` instead of just the two DataFrames.
- `aggregate_data()` now returns `(final_df, final_df_count)` instead of just `final_df`.