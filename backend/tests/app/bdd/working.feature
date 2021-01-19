# Created by nastya at 16.01.2021
Feature: All backend works
  In order to ensure user can use my app
  As a Developer
  I want to ...
  Scenario: Film evaluating scenario
    # Enter steps here
    Given I have user
    And I have films in database
    And I have context

    When I make login request
    Then I am logged in
    When I make film request
    Then I have films
    When I make film searching by given_genre request
    Then I have searched films
    When I make one film with genre request
    Then I have one film with genre data
    When I make film comments request
    Then I have film comments
    When I make create comment request with <given_text>
    Then I have new comment
    When I make create Like request with <given_value>
    Then I have new like
