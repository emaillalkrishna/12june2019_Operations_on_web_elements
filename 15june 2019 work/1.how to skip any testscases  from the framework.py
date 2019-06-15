# # # What is skip marker?



# # # Read data from the excel
# # # In this case we should understand that we are taking the value from excel.
# # # Inside the class before the method keep this

if ("excel_value" = "N"):
    @pytest.mark.skip(reason="Run flag set to No")