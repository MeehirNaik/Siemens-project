function displayData(xmlDoc) {
    const dataDiv = document.getElementById('data');
    const books = xmlDoc.getElementsByTagName('book');
    for (let i = 0; i < books.length; i++) {
      const book = books[i];
      const title = book.getElementsByTagName('title')[0].textContent;
      const author = book.getElementsByTagName('author')[0].textContent;
      const year = book.getElementsByTagName('year')[0].textContent;
      const bookDiv = document.createElement('div');
      bookDiv.innerHTML = `<strong>${title}</strong> by ${author} (${year})`;
      dataDiv.appendChild(bookDiv);
    }
  }
  