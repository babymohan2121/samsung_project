Feature:we want to valid the samsung mobile price
  @valid_data
  Scenario: valid the login page with valid data
    Given open browser as "Chrome"
    When enter URL as "https://www.google.com/"
    When type amazon in input box
    When click submit button
    When click amazon Link
    When type Samsung mobile
    When click search button
    Then verify the samsung mobile page is successsfully opened
    When click first link of samsung product
    When click AddtoCart