from test_script.scratch_exp.test_script_2508282354_homepage_rows_FASTTEXT_300_SMALL_5_5_3 import featured_studios_link
from test_script.scratch_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    featured_studios_link(driver_manager.get_driver())
    print("Test case 'featured_studios_link' executed successfully. ✅")
except Exception as e:
    print(f"featured_studios_link: Test case execution failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
