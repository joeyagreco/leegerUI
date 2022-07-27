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

function fixYearsInput() {
    const yearsInputElement = document.getElementById("years");
    const allowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]
    let validatedYearInputText = ""

    for (let i = 0; i < yearsInputElement.value.length; i++) {
        if (allowedCharacters.includes(yearsInputElement.value[i])) {
            validatedYearInputText = `${validatedYearInputText}${yearsInputElement.value[i]}`;
        }
    }
    yearsInputElement.value = validatedYearInputText;
    checkIfValidInput();
}

function isValidYearsInput(yearsStr) {
    if (yearsStr === "") {
        return false;
    }
    let years = yearsStr.split(",");
    console.log(years);
    for (let i = 0; i < years.length; i++) {
        const year = years[i]
        if (year === "") {
            continue;
        }
        if (year.length !== 4 || isNaN(year) || parseInt(year) < 1920 || parseInt(year) > 2200) {
            return false;
        }
    }
    return true;
}

function checkIfValidInput() {
    // does basic validation on league info and enables/disables download button accordingly
    const leagueId = document.getElementById("league-id").value;
    const years = document.getElementById("years").value;
    if (leagueId === "" || !isValidYearsInput(years)) {
        disableDownloadButton();
    } else {
        enableDownloadButton();
    }
}

function disableDownloadButton() {
    const downloadButton = document.getElementById("download-stats-button");
    downloadButton.classList.add("disabled")
    downloadButton.disabled = true;
}

function enableDownloadButton() {
    const downloadButton = document.getElementById("download-stats-button");
    downloadButton.classList.remove("disabled")
    downloadButton.disabled = false;
}