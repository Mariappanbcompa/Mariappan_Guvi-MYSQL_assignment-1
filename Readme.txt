# Warehouse Database Analysis Project

## Assignment Overview

**Assignment Title:** Warehouse Database Analysis  
**Skills Learned:** Python, MySQL  
**Domain:** MySQL  

## Problem Statement

A warehouse management system is a crucial component of the supply chain, responsible for controlling the storage and movement of materials within a warehouse. It also manages transactions like receiving, shipping, picking, and put away. The Warehouse Management System (WMS) optimizes stock putaway based on real-time bin utilization status. In this project, we'll work with a warehouse dataset to answer interesting questions.

## Approach

- The SQL file for creating and inserting data can be found [here](https://bit.ly/guvisql1).
- Import or execute the schema in any SQL server to build the database and tables in your local system.

## Assignment Questions

1. Select all warehouses.
2. Select all boxes with a value larger than $150.
3. Select all distinct contents in all the boxes.
4. Select the average value of all the boxes.
5. Select the warehouse code and the average value of the boxes in each warehouse.
6. Select only those warehouses where the average value of the boxes is greater than 150.
7. Select the code of each box, along with the name of the city the box is located in.
8. Select the warehouse codes, along with the number of boxes in each warehouse.
9. Optionally, take into account that some warehouses are empty (i.e., the box count should show up as zero, instead of omitting the warehouse from the result).
10. Select the codes of all warehouses that are saturated (a warehouse is saturated if the number of boxes in it is larger than the warehouse's capacity).
11. Select the codes of all the boxes located in Chicago.
12. Create a new warehouse in New York with a capacity for 3 boxes.
13. Create a new box, with code "H5RT," containing "Papers" with a value of $200 and located in warehouse 2.
14. Reduce the value of all boxes by 15%.
15. Remove all boxes with a value lower than $100.
16. Remove all boxes from saturated warehouses.
17. Add an index for the "Warehouse" column in the "boxes" table (Note: Index should NOT be used on small tables in practice).
18. Print all the existing indexes (Note: Index should NOT be used on small tables in practice).
19. Remove (drop) the index you added in step 17 (Note: Index should NOT be used on small tables in practice).

## Project Submission

Please submit the assignment notebook titled with your name and the assignment name through GitHub.

## Project Evaluation Metrics

- Write code in a modular fashion (in functional blocks).
- Maintainability: Code can be maintained as it grows.
- Portability: It works the same in every environment (operating system).
- Maintain your code on GitHub (Mandatory).
- Keep your GitHub repository public so anyone can check your code (Mandatory).
- Include a proper README file for project development (Mandatory).
- Include basic workflow and execution of the entire project in the README file on GitHub.
- Follow coding standards: [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- Create a demo video of your working model and post it on LinkedIn (Mandatory).

---
