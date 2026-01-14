terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "tfstate123"
    container_name       = "state"
    key                  = "aks.tfstate"
  }
}
