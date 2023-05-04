// Helper function to fetch an XML file
async function fetchXmlFile(filename) {
    const response = await fetch(filename);
    const xmlString = await response.text();
    return xmlString;
  }

  function readAllXmlFiles(folder) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", folder, false);
    xhttp.send();
  
    var fileNames = xhttp.responseText.split("\n");
    var xmlFiles = [];
  
    for (var i = 0; i < fileNames.length; i++) {
      if (fileNames[i].endsWith(".xml")) {
        var xhttp2 = new XMLHttpRequest();
        xhttp2.open("GET", folder + fileNames[i], false);
        xhttp2.send();
  
        var xmlDoc = xhttp2.responseXML;
        xmlFiles.push(xmlDoc);
      }
    }
  
    return xmlFiles;
  }
  
  // Helper function to parse an XML string and extract data
  function parseXmlString(xmlString) {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, 'text/xml');
    const serialNumber = xmlDoc.getElementsByTagName('SerialNumber')[0].textContent;
    const ipAddress = xmlDoc.getElementsByTagName('IPAddress')[0].textContent;
    const macAddress = xmlDoc.getElementsByTagName('MACAddress')[0].textContent;
    const hostname = xmlDoc.getElementsByTagName('HostName')[0].textContent;
    const bootTime = xmlDoc.getElementsByTagName('BootTime')[0].textContent;
    const readTime = new Date().toLocaleString();
    const item = {
      serialNumber,
      ipAddress,
      macAddress,
      hostname,
      bootTime,
      readTime
    };
    return item;
  }
  
  // Helper function to create an HTML table row from an object
  function createTableRow(item) {
    const row = document.createElement('tr');
    const serialNumberCell = document.createElement('td');
    serialNumberCell.innerText = item.serialNumber;
    row.appendChild(serialNumberCell);
    const ipAddressCell = document.createElement('td');
    ipAddressCell.innerText = item.ipAddress;
    row.appendChild(ipAddressCell);
    const macAddressCell = document.createElement('td');
    macAddressCell.innerText = item.macAddress;
    row.appendChild(macAddressCell);
    const hostnameCell = document.createElement('td');
    hostnameCell.innerText = item.hostname;
    row.appendChild(hostnameCell);
    const bootTimeCell = document.createElement('td');
    bootTimeCell.innerText = item.bootTime;
    row.appendChild(bootTimeCell);
    const readTimeCell = document.createElement('td');
    readTimeCell.innerText = item.readTime;
    row.appendChild(readTimeCell);
    return row;
  }
  
  // Helper function to create an HTML table from an array of objects
  function createTable(data) {
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');
    const serialNumberHeader = document.createElement('th');
    serialNumberHeader.innerText = 'Serial Number';
    headerRow.appendChild(serialNumberHeader);
    const ipAddressHeader = document.createElement('th');
    ipAddressHeader.innerText = 'IP Address';
    headerRow.appendChild(ipAddressHeader);
    const macAddressHeader = document.createElement('th');
    macAddressHeader.innerText = 'MAC Address';
    headerRow.appendChild(macAddressHeader);
    const hostnameHeader = document.createElement('th');
    hostnameHeader.innerText = 'Hostname';
    headerRow.appendChild(hostnameHeader);
    const bootTimeHeader = document.createElement('th');
    bootTimeHeader.innerText = 'Boot Time';
    headerRow.appendChild(bootTimeHeader);
    const readTimeHeader = document.createElement('th');
    readTimeHeader.innerText = 'Read Time';
    headerRow.appendChild(readTimeHeader);
    table.appendChild(headerRow);
    data.forEach(item => {
      const row = createTableRow(item);
      table.appendChild(row);
    });
    return table;
  }
  
  // Read XML files and parse data
  async function loadData() {
    const data = [];
    for (let i = 0; i < 10; i++) {
      const fileName = `serial_${i}.xml`;
      const fileContents = await fetchXmlFile(fileName);
      const item = parseXmlString(fileContents);
      data.push(item);
    }
    return data;
  }
  
  // Create HTML table and add to page
  async function main() {
    const data = await loadData();
    // Create table and add to page
    const table = createTable(data);
    document.body.appendChild(table);
  }

// Call main function
main();