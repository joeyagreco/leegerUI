function onDownloadStatsButtonPress() {
    const leagueId = document.getElementById("league-id").value;
    const fantasySite = document.getElementById("fantasy-site").value;
    const years = document.getElementById("years").value;
    const data = {
        "league_id": leagueId,
        "fantasy_site": fantasySite,
        "years": years
    };
    // send POST request
    let fetchPromise = post("/leeger", data);
    fetchPromise.then(response => {
        window.location.href = response.url;
    });
}

function validateYearsInput() {
    const yearsInputElement = document.getElementById("years");
    const allowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]
    let validatedYearInputText = ""

    for (let i = 0; i < yearsInputElement.value.length; i++) {
        if (allowedCharacters.includes(yearsInputElement.value[i])) {
            validatedYearInputText = `${validatedYearInputText}${yearsInputElement.value[i]}`;
        }
    }
    yearsInputElement.value = validatedYearInputText;
}