# Created by PARAhod at 7/6/2022
Feature: GitHub API validation
  # Enter feature description here

  @github
  Scenario: Session management check
    Given I have GitHub auth credentials
    When I hit /user/repos API of GitHub (https://api.github.com/user/repos)
    Then Status code of response should be 200
