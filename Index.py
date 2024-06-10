import streamlit as st

navbar = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
    <title>Stylish Navigation Bar</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        nav {
            background-color: white;
        }

        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        li {
            float: left;
        }

        li a {
            display: block;
            color: Black ;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }

        li a:hover {
            background-color: grey;
        }

        .content {
            padding: 20px;
            background-color: grey;
        }
    </style>
</head>
<body style="background-color:grey">
    <nav>
        <ul>
            <li><a href="/About" style='color: black'>About</a></li>
            <li><a href="/Contact" style='color: black'>Contact</a></li>
            <li><a href="/Homepage" style='color: black'>Main Menu</a></li>
        </ul>
    </nav>
        
</body>
</html>
'''

