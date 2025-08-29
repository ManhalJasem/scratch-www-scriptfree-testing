from test_script.scratch_exp.test_script_2508300043_navbar_FASTTEXT_300_SMALL_5_5_3 import create_when_signed_out
from test_script.scratch_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    create_when_signed_out(driver_manager.get_driver())
    print("Test case 'create_when_signed_out' executed successfully. ✅")
except Exception as e:
    print(f"create_when_signed_out: Test case execution failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
