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