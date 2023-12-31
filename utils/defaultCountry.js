const getCountry = () => {
  return fetch("https://ip2c.org/s")
    .then(response => response.text())
    .then(response => {
      const result = (response || "").toString();

      if (!result || result[0] !== "1") {
        console.warn("unable to fetch the country");
      }

      return result.substr(2, 2);
    });
};

export default getCountry;
