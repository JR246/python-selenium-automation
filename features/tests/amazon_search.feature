# Created by Jon at 11/25/2021
Feature: Tests for amazon search

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Search for table
    And Click search icon
    Then Search results have table
