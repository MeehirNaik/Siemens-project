var uniqueElements = [];
async function fetchXmlFiles() {
    try {
        const response = await fetch("./data/");
        if (!response.ok) {
            throw new Error(`Failed to fetch data. Server returned ${response.status} ${response.statusText}.`);
        }
        const text = await response.text();
        const parser = new DOMParser();
        const htmlDoc = parser.parseFromString(text, "text/html");
        const links = htmlDoc.querySelectorAll("a");
        const xmlLinks = Array.from(links).filter((link) => link.href.endsWith(".xml"));

        const allElements = [];
        for (const xmlLink of xmlLinks) {
            const xmlLinkParts = xmlLink.href.split("/");
            xmlLinkParts.splice(3, 0, "data");
            const xmlLinkWithDataset = xmlLinkParts.join('/');
            const response = await fetch(xmlLinkWithDataset);
            if (!response.ok) {
                throw new Error(`Failed to fetch XML data from ${xmlLinkWithDataset}. Server returned ${response.status} ${response.statusText}.`);
            }
            const xmlText = await response.text();
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(xmlText, "text/xml");
            const records = xmlDoc.querySelectorAll("SystemInfo");
            if (records.length === 0) {
                console.warn(`No SystemInfo elements found in ${xmlLinkWithDataset}. Skipping this file.`);
                continue;
            }
            for (const record of records) {
                const serialNumber = record.querySelector("SerialNumber");
                const ipAddress = record.querySelector("IPAddress");
                const macAddress = record.querySelector("MACAddress");
                const hostName = record.querySelector("HostName");
                const bootTime = record.querySelector("BootTime");
                if (!serialNumber || !ipAddress || !macAddress || !hostName || !bootTime) {
                    console.warn(`One or more required elements not found in SystemInfo element of ${xmlLinkWithDataset}. Skipping this record.`);
                    continue;
                }
                allElements.push(
                    serialNumber.textContent.trim(),
                    ipAddress.textContent.trim(),
                    macAddress.textContent.trim(),
                    hostName.textContent.trim(),
                    bootTime.textContent.trim()
                );
            }
        }

        // Create a Set to remove duplicates
        uniqueElements = new Set(allElements);

        // Convert Set back to an array and log it
        console.log(Array.from(uniqueElements));
        
		wordsArray = [...uniqueElements];
        console.log(wordsArray)
    } catch (error) {
        console.error(error);
    }
}

fetchXmlFiles();
