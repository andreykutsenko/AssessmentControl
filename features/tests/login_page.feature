# Created by KTS at 9/1/21
Feature: Automated tests for a login screen.

  @login1
  Scenario Outline: User verification with correct login and password
    Given Open login page
    When Filling <login> and <password> fields
    And Click Sign In button
    Then The <username> should be displayed correctly on the page
    Examples:
      | login             | password | username      |
      | student6@test.com | 12345    | Student Six   |

  @login2
  Scenario: New User Registration
    Given Open login page
    When Click Register Now link
    When Filling registration form
       | FirstName | LastName | Email              | GroupCode | Password |
       | John      | Travolta | travolta@gmail.com | ABC       | 12345    |
    And Click Register Me button
    Then Verify title "You have been Registered." on confirmation page

  @login3
  Scenario Outline: Submitting a password reset request
    Given Open login page
    When Click I forgot my password
    When Filling <email> field
    And Click Request Password Reset
    Then Verify title "Your request is confirmed" on confirmation page
    Examples:
      | email              |
      | student6@test.com |

  @login4
  Scenario Outline: Verification of the login with an empty Password field
    Given Open login page
    When Filling <email> field
    And Click Sign In button
    Then Verify "This field is required" on login page
    Examples:
      | email             |
      | student6@test.com |