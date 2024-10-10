from bs4 import BeautifulSoup
import json

alma_filepath = "alma.html"

if __name__ == "__main__":
    
    soup = BeautifulSoup(open(alma_filepath), "html.parser")

    trs = soup.find_all("tr")

    variables = dict()

    for tr in trs:

        tds = tr.find_all("td")

        if len(tds) != 8:
            continue

        alma, cmip, standard, long_name, unit, direction, dim, description = tds

        row = dict(
            short_name_alma=alma.text,
            short_name_cmip=cmip.text,
            standard_name=standard.text,
            long_name=long_name.text,
            unit=unit.text,
            direction=direction.text,
            dim=dim.text,
            description=description.text
        )

        variables[alma.text] = row

    json.dump(
        variables,
        open("alma.json", "w"),
        indent=4
    )

    # You will need to cut this off at the appropriate spots...