# Created by PARAhod at 7/4/2022
Feature: Verify if Books are added or deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which need to be added to Library
    When execute the AddBook Post API method
    Then the Book is added successfully
    And Status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality with different data
    Given the Book details which need to be added to Library with different <isbn> and <aisle>
    When execute the AddBook Post API method
    Then the Book is added successfully
    Examples:
      | isbn  | aisle |
      | taat  | 77    |
      | ogG!! | 9878  |
      | wqwq  | 100   |