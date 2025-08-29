from test_script.scratch_exp.test_script_2508271714_footer_links_FASTTEXT_300_SMALL_5_5_3 import click_DSA_requirements_link
from test_script.scratch_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    click_DSA_requirements_link(driver_manager.get_driver())
    print("Test case 'click_DSA_requirements_link' executed successfully. ✅")
except Exception as e:
    print(f"click_DSA_requirements_link: Test case execution failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
