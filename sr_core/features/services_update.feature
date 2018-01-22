# Created by Tymoteusz Paul at 18/01/2016
Feature: ServiceRegistry

 Background:
    Given there is a ServiceRegistry containing basic services

  Scenario Outline: updating a service:
    When I update a service of id "<service_id>" by changing its name to "<new_name>" or its version to "<new_version>"
    Then I should be notified with a change "<change>"
    Examples:
      | service_id | new_name      | new_version  | change  |
      | 1          | updated_name2 | 2.0.1        | changed |