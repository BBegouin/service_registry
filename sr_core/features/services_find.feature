# Created by Tymoteusz Paul at 18/01/2016
Feature: ServiceRegistry

  Background:
    Given there is a ServiceRegistry containing basic services

  Scenario Outline: Finding service without version:
    When I search for a service "<service>" without version
    Then I should find count "<count>" services
    Examples:
      | service | count |
      | test    |   4   |
      | test2   |   2   |

  Scenario Outline: Find service:
    When I search for a service "<service>" with version "<version>"
    Then I should find count "<count>" services
    And the service "<service>" should have the correct version "<version>"
    Examples:
      | service | version | count |
      | test    | 0.0.1   |   2   |
      | test    | 0.0.2   |   2   |
      | test2   | 0.0.2   |   2   |

  Scenario Outline: Finding non existing service:
    When I search for a service "<service>" with version "<version>"
    Then I should find count "<count>" services
    Examples:
      | service | version | count |
      | test    | 0.0.4   |   0   |
      | test3    | 0.0.1   |   0   |