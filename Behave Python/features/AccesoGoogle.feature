# Created by juan pablo pedraza
Feature:  Training
  # Enter feature description here

  Scenario: Navegación a la página de Google
    Given I navigate to Google Home Page
    Then I see the page title as "Instagram"
    And I see the login button