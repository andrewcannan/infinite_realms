# Testing and Validation
----------------

<img src="./documentation/responsiveness/responsive-mockup.png">
<br><br>

**[Link to the Deployed Site](https://infinite-realms-366e4ca2f09e.herokuapp.com/)**
<br><br>
----------------

## Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [Python Validation](#python-validation)
    * [Lighthouse Reports](#lighthouse-report)
    * [WAVE Accessibility](#wave-accessibility-checker)
<br><br>

----------------

## Validation

### HTML Validation

All pages tested for  HTML Validation at [W3C markup validation service](https://validator.w3.org/)  with no errors or warnings.

<details>
<summary>Homepage</summary>
<br>
<img src="documentation/html_validation/home-html-validation.png">
</details>
<details>
<summary>Products</summary>
<br>
<img src="documentation/html_validation/products-html-validation.png">
</details>
<details>
<summary>Product Detail</summary>
<br>
<img src="documentation/html_validation/product-detail-html-validation.png">
</details>
<details>
<summary>Add Product</summary>
<br>
<img src="documentation/html_validation/add-product-html-validation.png">
</details>
<details>
<summary>Edit Product</summary>
<br>
<img src="documentation/html_validation/edit-product-html-validation.png">
</details>
<details>
<summary>Add Review</summary>
<br>
<img src="documentation/html_validation/add-review-html-validation.png">
</details>
<details>
<summary>Edit Review</summary>
<br>
<img src="documentation/html_validation/edit-review-html-validation.png">
</details>
<details>
<summary>Bag</summary>
<br>
<img src="documentation/html_validation/bag-html-validation.png">
</details>
<details>
<summary>Checkout</summary>
<br>
<img src="documentation/html_validation/checkout-html-validation.png">
</details>
<details>
<summary>Checkout Success</summary>
<br>
<img src="documentation/html_validation/checkout-success-html-validation.png">
</details>
<details>
<summary>Register</summary>
<br>
<img src="documentation/html_validation/register-html-validation.png">
</details>
<details>
<summary>Login</summary>
<br>
<img src="documentation/html_validation/login-html-validation.png">
</details>
<details>
<summary>Logout</summary>
<br>
<img src="documentation/html_validation/logout-html-validation.png">
</details>
<details>
<summary>Contact</summary>
<br>
<img src="documentation/html_validation/contact-html-validation.png">
</details>
<details>
<summary>Profile</summary>
<br>
<img src="documentation/html_validation/profile-html-validation.png">
</details>
<details>
<summary>404</summary>
<br>
<img src="documentation/html_validation/404-html-validation.png">
</details>
<br><br>

### CSS Validation

All static CSS files pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors.

<details>
<summary>base.css</summary>
<br>
<img src="documentation/css_validation/base-css-validation.png">
</details>
<details>
<summary>checkout.css</summary>
<br>
<img src="documentation/css_validation/checkout-css-validation.png">
</details>
<details>
<summary>profile.css</summary>
<br>
<img src="documentation/css_validation/profile-css-validation.png">
</details>
<br><br>

### JS Validation

JS files and scripts on templates run through [JShint](https://jshint.com/) for validation with no errors.

<details>
<summary>Scripts for update and remove links on Bag template.</summary>
<br>
<img src="documentation/js_validation/update-and-remove-js-validation.png">
</details>
<details>
<summary>Script to disable first option in select on Contact us template.</summary>
<br>
<img src="documentation/js_validation/disable-first-contact-select-js-validation.png">
</details>
<details>
<summary>Script to update the text on image update on Add product and Edit product templates.</summary>
<br>
<img src="documentation/js_validation/new-image-text-js-validation.png">
</details>
<details>
<summary>Script for back to top button on products template.</summary>
<br>
<img src="documentation/js_validation/back-to-top-button-script-js-validation.png">
</details>
<details>
<summary>Script to add arguements to URL on change of sort selector on products template.</summary>
<br>
<img src="documentation/js_validation/sort-selector-script-js-validation.png">
</details>
<details>
<summary>coutnryfield.js</summary>
<br>
<img src="documentation/js_validation/countryfield-js-validation.png">
</details>
<details>
<summary>stripe-elements.js</summary>
<br>
<img src="documentation/js_validation/stripe-elements-js-validation.png">
</details>
<details>
<summary>get_sub_categories_script.html</summary>
<br>
<img src="documentation/js_validation/get-sub-categories-script-js-validation.png">
</details>
<details>
<summary>quantity_input_script.html</summary>
<br>
<img src="documentation/js_validation/quantity-input-script-js-validation.png">
</details>
<br><br>

### Python Validation

Pylance used during development to detect errors and PEP8 compliance, but code also run through [CI PEP8 Linter](https://pep8ci.herokuapp.com/) and passed with no warnings.

#### Root Level
<details>
<summary>custom-storages.py</summary>
<br>
<img src="documentation/python_validation/custom_storages.py-validation.png">
</details>
<details>
<summary>manage.py</summary>
<br>
<img src="documentation/python_validation/manage.py-validation.png">
</details>

#### Infinite Realms 
<details>
<summary>asgi.py</summary>
<br>
<img src="documentation/python_validation/infinite_realms-asgi.py-validation.png">
</details>
<details>
<summary>settings.py</summary>
<br>
<img src="documentation/python_validation/infinite_realms-settings.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/infinite_realms-urls.py-validation.png">
</details>
<details>
<summary>wsgi.py</summary>
<br>
<img src="documentation/python_validation/infinite_realms-wsgi.py-validation.png">
</details>

#### Bag App
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/bag-apps.py-validation.png">
</details>
<details>
<summary>contexts.py</summary>
<br>
<img src="documentation/python_validation/bag-contexts.py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="documentation/python_validation/bag-forms.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/bag-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/bag-views.py-validation.png">
</details>
<details>
<summary>templatetags/bag_tools.py</summary>
<br>
<img src="documentation/python_validation/bag-templatetags-bag_tools.py-validation.png">
</details>

#### Checkout App
<details>
<summary>admin.py</summary>
<br>
<img src="documentation/python_validation/checkout-admin.py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/checkout-apps.py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="documentation/python_validation/checkout-models.py-validation.png">
</details>
<details>
<summary>signals.py</summary>
<br>
<img src="documentation/python_validation/checkout-signals.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/checkout-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/checkout-views.py-validation.png">
</details>
<details>
<summary>webhook_handler.py</summary>
<br>
<img src="documentation/python_validation/checkout-webhook_handler.py-validation.png">
</details>
<details>
<summary>webhooks.py</summary>
<br>
<img src="documentation/python_validation/checkout-webhooks.py-validation.png">
</details>

#### Contact App
<details>
<summary>admin.py</summary>
<br>
<img src="documentation/python_validation/contact-admin.py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/contact-apps.py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="documentation/python_validation/contact-forms.py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="documentation/python_validation/contact-models.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/contact-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/contact-views.py-validation.png">
</details>

#### Home App
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/home-apps.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/home-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/home-views.py-validation.png">
</details>

#### Products App
<details>
<summary>admin.py</summary>
<br>
<img src="documentation/python_validation/products-admin.py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/products-apps.py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="documentation/python_validation/products-forms.py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="documentation/python_validation/products-models.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/products-urls,py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/products-views.py-validation.png">
</details>
<details>
<summary>widgets.py</summary>
<br>
<img src="documentation/python_validation/products-widgets.py-validation.png">
</details>

#### Profiles App
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/profiles-apps.py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="documentation/python_validation/profiles-forms.py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="documentation/python_validation/profiles-models.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/profiles-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/profiles-views.py-validation.png">
</details>

#### Reviews App
<details>
<summary>admin.py</summary>
<br>
<img src="documentation/python_validation/reviews-admin.py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="documentation/python_validation/reviews-apps.py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="documentation/python_validation/reviews-forms.py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="documentation/python_validation/reviews-models.py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="documentation/python_validation/reviews-urls.py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="documentation/python_validation/reviews-views.py-validation.png">
</details>
<br><br>

### Lighthouse Report

[Chrome DevTools' Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the site. Unfortunately, Best Practices was only ever 95 across the site instead of a desirable 100, investigation pointed towards warnings that cross-site cookies from Stripe will be blocked in future chrome versions. Looking into this, Stripe say they are endeavouring to continuely add support for this.

<details>
<summary>Homepage - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/home-lighthouse.png">
</details>
<details>
<summary>Products - Performance only 89, but given there was 64 products on that page decided to overlook for now, as a page with just 9 products had a score of 93. Potentially pagination could be used to raise the performance value. SEO also only just 90 belive this to be checking the page as a superuser and Google warning of uncrawlable delete links, this would not affect a normal user.</summary>
<br>
<img src="documentation/lighthouse_reports/products-lighthouse.png">
<img src="documentation/lighthouse_reports/products-funkos-lighthouse.png">
</details>
<details>
<summary>Product Detail - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/product-detail-lighthouse.png">
</details>
<details>
<summary>Add Product - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/add-product-lighthouse.png">
</details>
<details>
<summary>Edit Product - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/edit-product-lighthouse.png">
</details>
<details>
<summary>Add Review - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/add-review-lighthouse.png">
</details>
<details>
<summary>Edit Review - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/edit-review-lighthouse.png">
</details>
<details>
<summary>Bag - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/bag-lighthouse.png">
</details>
<details>
<summary>Checkout - Scores above 90</summary>
<br>
<img src="documentation/lighthouse_reports/checkout-lighthouse.png">
</details>
<details>
<summary>Checkout Success - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/checkout-success-lighthouse.png">
</details>
<details>
<summary>Register - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/register-lighthouse.png">
</details>
<details>
<summary>Login - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/login-lighthouse.png">
</details>
<details>
<summary>Logout - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/logout-lighthouse.png">
</details>
<details>
<summary>Contact - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/contact-lighthouse.png">
</details>
<details>
<summary>Profile - Scores above 90.</summary>
<br>
<img src="documentation/lighthouse_reports/profile-lighthouse.png">
</details>
<br><br>

### WAVE Accessibility Checker

[WAVE](https://wave.webaim.org/) was used to ensure that site is also accessible to individuals with disabilities. WAVE effectively spots various accessibility and Web Content Accessibility Guideline (WCAG) issues, which are subsequently addressed based on the initial assessment outcomes.

<details>
<summary>Homepage - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-home.png">
</details>
<details>
<summary>Products - 0 Errors, 1 Alert for possible headings for price on product cards. Ignored as not meant to be heading.</summary>
<br>
<img src="documentation/wave_reports/wave-report-products.png">
</details>
<details>
<summary>Product Detail - 0 Errors, 1 Alert for same possible heading for price.</summary>
<br>
<img src="documentation/wave_reports/wave-report-product-detail.png">
</details>
<details>
<summary>Add Product - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-add-product.png">
</details>
<details>
<summary>Edit Product - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-edit-product.png">
</details>
<details>
<summary>Add Review - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-add-review.png">
</details>
<details>
<summary>Edit Review - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-edit-review.png">
</details>
<details>
<summary>Bag - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-bag.png">
</details>
<details>
<summary>Checkout - 1 Contrast Error. Points to placeholder in Country Select, decided to leave as its the same color as the other placeholders which pass contrast check. 1 Alert for skipped heading level but H1, H2, H3, H4 and H5 all present.</summary>
<br>
<img src="documentation/wave_reports/wave-report-checkout.png">
</details>
<details>
<summary>Checkout Success - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-checkout-success.png">
</details>
<details>
<summary>Register - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-register.png">
</details>
<details>
<summary>Login - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-login.png">
</details>
<details>
<summary>Logout - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-logout.png">
</details>
<details>
<summary>Contact - 0 Errors, 1 Alert for redundant link. Points to home link in footer being redundant as also present in header. Strangely enough only present on this page, also as header link isn't available to mobile users it acts as a convenient link back to the homepage.</summary>
<br>
<img src="documentation/wave_reports/wave-report-contact.png">
</details>
<details>
<summary>Profile - 1 Contrast error on same Country Select as checkout.html.</summary>
<br>
<img src="documentation/wave_reports/wave-report-profile.png">
</details>
<details>
<summary>Enquiries - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-enquiries.png">
</details>
<details>
<summary>Send Response - 0 Errors or Alerts.</summary>
<br>
<img src="documentation/wave_reports/wave-report-send_response.png">
</details>
<details>
<summary>404 - 0 Errors 1 alert. Redundant link back to homepage.</summary>
<br>
<img src="documentation/wave_reports/wave-report-404.png">
</details>
<br><br>
