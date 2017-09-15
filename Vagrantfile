# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.synced_folder "./", "/vagrant"
  config.vm.provider "vmware_fusion" do |vmware|
    vmware.memory = "2048"
  end
end
