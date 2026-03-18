# User Input Validation System

## Overview

This program collects user input for:

* Email address
* Phone number
* Password

It then validates each input using basic logical checks and prints error messages if the input is invalid.

---

## Core Logic

### 1. Email Validation

Function: `validate_email(email)`

Checks:

* Input is not empty
* Contains `@`
* Contains `.com`

If any condition fails, an error message is printed.

---

### 2. Phone Number Validation

Function: `validate_phone(phone)`

Checks:

* Input is not empty
* Must be exactly 10 digits
* Must contain only numbers
* Must start with `07` (Kenyan format)

Prints appropriate error messages for invalid input.

---

### 3. Password Validation

Function: `validate_password(password)`

Checks:

* Input is not empty
* Must be at least 8 characters long
* Must contain at least one number

Prints error messages if conditions are not met.

---

## Program Flow

1. User is prompted to enter:

   * Email
   * Phone number
   * Password

2. Each input is passed to its respective validation function.

3. Functions print error messages if validation fails.

---

## Key Notes

* Functions always return `True`, but validation feedback is given through printed messages.
* Multiple validation errors can be shown at once.
* The program does not stop execution on invalid input.

---

## Summary

This project demonstrates:

* Basic input validation
* Use of functions
* Conditional logic
* Handling user input

---
