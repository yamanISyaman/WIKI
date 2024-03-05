# CS50 Web Programming: Wiki Project

## Background

Wikipedia is a free online encyclopedia consisting of numerous encyclopedia entries on various topics. This project aims to create a simplified version of Wikipedia using Python and JavaScript, focusing on storing encyclopedia entries in Markdown instead of HTML for ease of writing and editing.

## Specifications

### Entry Page

- Visiting `/wiki/TITLE` should render a page displaying the contents of that encyclopedia entry.
- If an entry does not exist, an error page indicating the requested page was not found is presented.

### Index Page

- Update `index.html` to allow users to click on any entry name to be taken directly to that entry page.

### Search

- Users can search for an encyclopedia entry by typing a query into the search box.
- If the query matches an entry, the user is redirected to that entry’s page.
- If the query does not match, the user is taken to a search results page displaying entries with the query as a substring.

### New Page

- Clicking “Create New Page” allows users to create a new encyclopedia entry.
- Users can enter a title and Markdown content for the page.
- If an entry with the provided title already exists, an error message is presented.

### Edit Page

- Users can edit an entry’s Markdown content from the entry page.
- The `textarea` is pre-populated with the existing Markdown content.

### Random Page

- Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

- Markdown content in the entry file is converted to HTML before being displayed to the user.
- A challenge for more comfortable developers is to implement the conversion without external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs.
