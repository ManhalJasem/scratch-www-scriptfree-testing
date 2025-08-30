from test_script.scratch_exp.test_script_2508300143_search_FASTTEXT_300_SMALL_5_5_3 import switching_to_studios_maintains_search_string
from test_script.scratch_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    switching_to_studios_maintains_search_string(driver_manager.get_driver())
    print("Test case 'switching_to_studios_maintains_search_string' executed successfully. ✅")
except Exception as e:
    print(f"switching_to_studios_maintains_search_string: Test case execution failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
