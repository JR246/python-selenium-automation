# Created by Jon at 11/27/2021
Feature: Test Case for Help search

  Scenario: user can search for help on Amazon
    Given Open Amazon Help page
    When Search for search field
    # And Click on search icon in search page
    Then Search results for Cancel Items or Orders