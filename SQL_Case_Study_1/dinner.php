<!DOCTYPE html>
<html>

<head>
  <title>SQL Query Results</title>
</head>

<body>

  <?php
  $servername = "localhost";
  $username = "root";
  $password = "";
  $database = "dannys_diner";

  // Create a connection to the database
  $conn = new mysqli($servername, $username, $password, $database);

  // Check the connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  // Define an array of SQL queries
  $queries = [
    // SQL Query 1
    "SELECT customer_id, SUM(price) AS total_sale
     FROM sales s
     JOIN menu m ON s.product_id = m.product_id
     GROUP BY customer_id
     ORDER BY customer_id",

    // SQL Query 2
    "SELECT customer_id, COUNT(DISTINCT(order_date)) AS number_of_visits
     FROM sales
     GROUP BY customer_id",

    // SQL Query 3
    "SELECT customer_id, product_name, order_date
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE order_date = '2021-01-01' 
     GROUP BY customer_id",

    // SQL Query 4
    "SELECT product_name, COUNT(product_name) times_purchased
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     GROUP BY product_name
     ORDER BY times_purchased DESC
     LIMIT 1",

    // SQL Query 5
    "SELECT customer_id, product_name, COUNT(product_name) times_purchased
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     GROUP BY customer_id, product_name
     ORDER BY times_purchased DESC",

    // SQL Query 6 (Customer A)
    "SELECT customer_id, order_date, product_name 
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'A' AND order_date > '2021-01-07'
     ORDER BY order_date
     LIMIT 1",

    // SQL Query 6 (Customer B)
    "SELECT customer_id, order_date, product_name 
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'B' AND order_date > '2021-01-09'
     ORDER BY order_date
     LIMIT 1",

    // SQL Query 7 (Customer A, dates before membership)
    "SELECT customer_id, order_date, product_name 
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'A' AND order_date < '2021-01-07'
     ORDER BY order_date DESC",

    // SQL Query 7 (Customer B, dates before membership)
    "SELECT customer_id, order_date, product_name 
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'B' AND order_date < '2021-01-09'
     ORDER BY order_date DESC
     LIMIT 1",

    // SQL Query 8 (Customer A, total items and amount spent)
    "SELECT customer_id, order_date, COUNT(product_name) total_items, SUM(price) amount_spent
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'A' AND order_date < '2021-01-07'
     GROUP BY customer_id
     ORDER BY order_date",

    // SQL Query 8 (Customer B, total items and amount spent)
    "SELECT customer_id, order_date, COUNT(product_name) total_items, SUM(price) amount_spent
     FROM sales
     LEFT JOIN menu 
       ON sales.product_id = menu.product_id
     WHERE customer_id = 'B' AND order_date < '2021-01-09'
     GROUP BY customer_id
     ORDER BY order_date",

    // SQL Query 9
    "SELECT customer_id,
    SUM(CASE
        WHEN product_name = 'sushi' THEN 20 * price
        ELSE 10 * price
    END) total_points
    FROM sales
    LEFT JOIN menu 
      ON sales.product_id = menu.product_id
    GROUP BY customer_id",


    // SQL Query 10
    "WITH cte_OfferValidity AS 
        (SELECT s.customer_id, m.join_date, s.order_date,
            date_add(m.join_date, interval(6) DAY) firstweek_ends, menu.product_name, menu.price
        FROM sales s
        LEFT JOIN members m
          ON s.customer_id = m.customer_id
        LEFT JOIN menu
            ON s.product_id = menu.product_id)
    SELECT customer_id,
        SUM(CASE
                WHEN order_date BETWEEN join_date AND firstweek_ends THEN 20 * price 
                WHEN (order_date NOT BETWEEN join_date AND firstweek_ends) AND product_name = 'sushi' THEN 20 * price
                ELSE 10 * price
            END) points
    FROM cte_OfferValidity
    WHERE order_date < '2021-02-01' -- filter jan points only
    GROUP BY customer_id"
  ];
  echo "
  <h3> Queries </h3>
  1. What is the total amount each customer spent at the restaurant?<br>
  2. How many days has each customer visited the restaurant?<br>
  3. What was the first item from the menu purchased by each customer?<br>
  4. What is the most purchased item on the menu and how many times was it purchased by all customers?<br>
  5. Which item was the most popular for each customer?<br>
  6. Which item was purchased first by the customer after they became a member?<br>
  7. Which item was purchased just before the customer became a member?<br>
  8. What is the total items and amount spent for each member before they became a member?<br>
  9. If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?<br>
  10.In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?<br>
  ";
  // Execute and display results for each query
  foreach ($queries as $index => $query) {
    $result = $conn->query($query);

    echo "<h5>Query Results</h5>";

    if ($result->num_rows > 0) {
      echo "<table border='1' style='text-align: center;'>";
      $headerPrinted = false;
      while ($row = $result->fetch_assoc()) {
        if (!$headerPrinted) {
          echo "<tr>";
          foreach ($row as $key => $value) {
            echo "<th>" . $key . "</th>";
          }
          echo "</tr>";
          $headerPrinted = true;
        }
        echo "<tr>";
        foreach ($row as $value) {
          echo "<td>" . $value . "</td>";
        }
        echo "</tr>";
      }
      echo "</table>";
    } else {
      echo "No records found for Query ";
    }

    echo "<br>";
  }

  // Close the database connection
  $conn->close();
  ?>

</body>

</html>