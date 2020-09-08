package controller

import (
	"encoding/json"
	"net/http"

	"github.com/ExitoLab/spinnaker_gamification_app/github"
)

func GetIssue(w http.ResponseWriter, r *http.Request) {
	// some logic here
	issues := github.GetIssues("ExitoLab", "spinnaker-ms-teams-notification-plugin")

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(issues)
}
