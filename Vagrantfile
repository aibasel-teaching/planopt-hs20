semester = "planopt-hs20"

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 3
  end

  config.vm.provision "shell", :args => [semester], inline: <<-SHELL
    apt-get update && apt-get install --no-install-recommends -y \
        bison      \
        cmake      \
        ecl        \
        emacs      \
        flex       \
        g++        \
        git        \
        libffi-dev \
        make       \
        meld       \
        python     \
        xauth

    git clone "https://github.com/aibasel-teaching/${1}.git" "/vagrant/${1}"

    git clone https://github.com/KCL-Planning/VAL.git VAL
    cd VAL
    git checkout a5565396007eee73ac36527fbf904142b3077c74
    make clean
    sed -i 's/-Werror //g' Makefile  # Ignore warnings.
    make
    sudo mv validate /usr/bin
    cd ..
    rm -rf VAL
    
    git clone https://github.com/patrikhaslum/INVAL.git INVAL
    cd INVAL
    sed -i '1s|.*|#!/usr/bin/ecl -shell|g' compile-with-ecl
    ./compile-with-ecl
    sudo mv inval /usr/bin
    cd ..
    rm -rf INVAL
    
    
    cd "/vagrant/${1}/demo/fast-downward"
    ./build.py
  SHELL

  config.ssh.forward_x11 = true
  config.ssh.forward_agent = true
end
