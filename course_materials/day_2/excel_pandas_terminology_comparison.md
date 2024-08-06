# Comparison between Excel Terminology and pandas Terminology

| **Excel Terminology** | **pandas Terminology** | **Description**                                |
|-----------------------|------------------------|------------------------------------------------|
| Worksheet             | DataFrame              | A single spreadsheet within a workbook. In pandas, a DataFrame is a 2-dimensional labeled data structure. |
| Column                | Series                 | A vertical stack of cells in a worksheet. In pandas, a Series is a one-dimensional labeled array. |
| Row                   | Series                 | A horizontal stack of cells in a worksheet. Rows in pandas are also represented by Series objects when selected. |
| Named Range           | Named Index/Column     | A user-defined name for a cell or range of cells. In pandas, similar functionality is achieved by naming indices or columns. |
| Cell                  | DataFrame Cell         | A single data point within a worksheet, addressed by its column and row. In pandas, it's an element within a DataFrame. |
| Range                 | DataFrame Slice        | A selection of cells in a worksheet, which can be contiguous or non-contiguous. In pandas, a slice refers to a subset of rows or columns from a DataFrame. |
| SUM, AVERAGE, etc.    | sum(), mean(), etc.    | Functions for performing aggregate calculations. In pandas, similar operations are available as methods. |
| Filter                | Query/Filter           | A way to display only the rows that meet certain criteria. In pandas, filtering is done using boolean indexing or the `query` method. |
| Sorting               | sort_values()          | Arranging data in a specified order. In pandas, sorting is done using the `sort_values` method. |
| Formula               | Expression/Method      | An equation used to calculate values based on other cell values. In pandas, similar calculations are performed using expressions or methods. |
| Table                 | DataFrame              | A structured range with its own sorting and filtering. In pandas, a DataFrame inherently supports these operations using filters |
| Pivot Table           | pivot_table            | A tool for summarizing data by categories and aggregating it. In pandas, this is done using the `pivot_table` method. |
| VLOOKUP               | merge()/join()         | A function to look up values in a table based on a key. In pandas, `merge` or `join` methods are used for similar operations. |
| Data Validation       | Validation             | Rules to control what data can be entered into a cell. In pandas, validation can be implemented using custom functions or packages. |
| Chart                 | Plot                   | A graphical representation of data. In pandas, plotting functions can be used to create visualizations|
| Macro                 | Script/Function        | A set of instructions to automate tasks. In pandas, similar automation is achieved through scripting functions. |
| Conditional Formatting| Conditional Formatting | Applying formatting to cells based on their values. In pandas, this can be achieved using styling functions. |
| Data Import/Export    | read_*/to_* methods    | Loading data from and saving data to external sources. In pandas, there are `read_*` and `to_*` methods for various formats (CSV, Excel, SQL, etc.). |
