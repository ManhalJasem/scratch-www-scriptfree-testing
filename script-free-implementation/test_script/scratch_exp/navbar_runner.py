from test_script.scratch_exp.test_script_2508300021_navbar_FASTTEXT_300_SMALL_5_5_3 import search_bar_test
from test_script.scratch_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    search_bar_test(driver_manager.get_driver())
    print("Test case 'search_bar_test' executed successfully. ✅")
except Exception as e:
    print(f"search_bar_test: Test case execution failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
