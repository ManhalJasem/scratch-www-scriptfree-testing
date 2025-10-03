# Script-Free Testing on Scratch-www

This project integrates the *script-free* GUI-testing technique introduced by Kirinuki *et al.* (ICSME 2021 & SANER 2022). Instead of brittle, locator-based Selenium code, each test step is expressed in plain English (e.g., `click "Sign in"`), and the framework uses NLP and heuristic search to identify the correct element at runtime.

We evaluate this approach on the [Scratch-www](https://github.com/scratchfoundation/scratch-www) web application by comparing **normal locator-based tests** with **script-free tests**.

---

## Objectives

- **Lower maintenance costs** by eliminating explicit locators and reducing test flakiness after UI changes.  
- **Assess robustness** of the script-free approach on a widely used, evolving web platform.  
- **Provide reproducible benchmarks** so others can compare against traditional locator-repair techniques.  

---

## Getting Started

### 1 · Prerequisites

| Tool        | Recommended Version | Notes                                        |
| ----------- | ------------------- | -------------------------------------------- |
| **Node.js** | ≥ 14                | Required for Scratch-www development/test.   |
| **Python**  | ≥ 3.9               | Needed for the script-free test runner.      |

*Note*: Follow the tutorial on this [Scratch-www](https://github.com/scratchfoundation/scratch-www) page if you encounter any problems. Also check the [issues](https://github.com/scratchfoundation/scratch-www/issues) page.

---

## Running Scratch-www Tests

### 1 · Setup the Scratch-www Environment

```bash
nvm use 14
npm install
npm run build
```

This script installs dependencies, and builds the app.
After these steps follow the readme page in [script-free-implementation](script-free-implementation/readme.md) to setup script-free.


---

### 2 · Run Normal Tests

```bash
./run-test.sh
```

Executes the **locator-based Selenium tests** on Scratch-www.  
**Expected result:** Tests may fail after GUI changes due to fragile locators.

---

### 3 · Run Script-Free Tests

```bash
./run_scriptfree_test.sh
```

Executes the **script-free tests** driven by natural-language steps.  
**Expected result:** More resilient to UI changes than locator-based tests.

---

## Scratch-www Locator Changes — Commits

The table below summarizes the commits related to locator changes and their outcomes in normal vs. script-free testing.

| Commit SHA | File(s) affected | Results Description | Number of test cases | Test cases run in script-free | Converted cases | Locator changes | Script-free passes (tests) | Script-free passes (locators) | Test case pass rate (%) | Locator pass rate (%) |
| ---------- | ---------------- | ------------------- | -------------------- | ----------------------------- | --------------- | --------------- | -------------------------- | ----------------------------- | ----------------------- | --------------------- |
| a3af523ca99da87e0ccff75df0bef07f8216a482 | `test/integration/footer-links.test.js` | 1 of 1 test cases run in script-free; 1 of 1 locator change passed in script-free | 1 | 1 | 1 | 1 | 1 | 1 | 100 | 100 |
| bf91904a33ab4d792b1599d7ef7550d5dd561b15 | `homepage_rows.test.js` | Test case converted, but script-free failed to detect the correct element (multiple elements with same class). Normal test succeeds, script-free fails. | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 7a5bdc040064ff56eff4fe41207e03777ef3b525 | `navbar.test.js` | 1 of 1 test cases run in script-free; 1 of 1 locator change passed in script-free | 1 | 1 | 1 | 1 | 1 | 1 | 100 | 100 |
| 0cd1f6e6bee478436c537785c37dbe4204bdb04d | `navbar.test.js` | Same test case as above; script-free passed | 1 | 1 | 1 | 1 | 1 | 1 | 100 | 100 |
| 37d279f6e5b925ed388a78ae3fbfca0fac4b46da | `navbar.test.js` | Locator change altered the entire element; script-free still passed | 1 | 1 | 1 | 1 | 1 | 1 | 100 | 100 |
| d7fdb4729fd5896ce9ec07a28cb453de12d3a41b | `search.test.js` | 1 of 1 test cases run in script-free; 1 of 1 locator change passed in script-free | 1 | 1 | 1 | 1 | 1 | 1 | 100 | 100 |

---

## Example Branch Pairs for Locator-Change Experiments

| Before app change (baseline)   | After app change, **before** locator change   | After app change **and** locator change   | Impacted files/tests (examples)      |
| ------------------------------- | --------------------------------------------- | ----------------------------------------- | ------------------------------------ |
| `before_app_change_<sha>`       | `after_app_change_before_locator_change_<sha>`| `after_app_change_and_locator_change_<sha>`| `ui/LoginTest.js, ui/ProfileTest.js` |

**Descriptions**

- **Before app change**  
  Snapshot of Scratch-www before the UI changes that cause locator failures.  

- **After app change and before locator change**  
  Scratch-www with UI modifications but **without** locator fixes. Normal tests expected to fail.  

- **After app change and locator change**  
  Scratch-www with UI modifications **and** updated locators. Both normal and script-free tests should pass.  

---

## Example Experiment Flow

1. **Verify failures on the “after app change, before locator change” branch**
   ```bash
   git checkout after_app_change_before_locator_change_<sha>
   npm install
   npm run build
   ./run-test.sh  # If you encounter any issue with chromedrivers, try installing appropriate chrome/chromedriver version
   ```
   **Expected result:** Normal tests fail due to outdated locators.

2. **Run script-free on the “before app change” branch**
   ```bash
   git checkout before_app_change_<sha>
   npm install
   npm run build
   ./run_scriptfree_test.sh
   ```
   **Expected result:** Script-free tests succeed (baseline).  

3. **Run script-free on the “after app change, before locator change” branch**
   ```bash
   git checkout after_app_change_before_locator_change_<sha>
   npm install
   npm run build
   ./run_scriptfree_test.sh
   ```
   **Expected result:** Script-free tests remain functional even when normal tests fail.  

4. **Confirm success on the “after app change and locator change” branch**
   ```bash
   git checkout after_app_change_and_locator_change_<sha>
   npm install
   npm run build
   ./run-test.sh
   ./run_scriptfree_test.sh
   ```
   **Expected result:** Both normal and script-free tests succeed.  

---

## Expected Results

- **Normal tests** → Failures likely if UI locators changed.  
- **Script-free tests** → Should succeed in many cases despite UI changes, showing improved robustness.  

---

## Further Reading

- Kirinuki *et al.* “NLP-Assisted Web Element Identification Toward Script-Free Testing” — ICSME 2021.  
- Kirinuki *et al.* “Web Element Identification by Combining NLP and Heuristic Search for Web Testing” — SANER 2022.  
- Scratch-www project: https://github.com/scratchfoundation/scratch-www  