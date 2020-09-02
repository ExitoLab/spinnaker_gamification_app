package models

type issues struct {
	ID    uint   `json:"id" gorm:"primary_key"`
	Title string `json:"title"`
	URL   string `json:"url"`
}
