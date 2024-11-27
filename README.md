# gnuradio-projects
This repository shares my experience in Software Defined Radio (SDR), and I have updated it with relevant projects or links in the field. It provides a step-by-step guide to understanding and implementing SDR using the GNU Radio Toolkit and includes easy-to-use examples to help newcomers get started in the field. Some guides are in Spanish, as they are materials created for my work as a teacher in this field when I taught at the  Instituto Tecnológico Metropolitano de Medellín.

# Related Links
-(https://github.com/gnuradio/gnuradio)

- (https://wiki.gnuradio.org/index.php?title=Tutorials)

- (https://files.ettus.com/manual/page_install.html)

-----------------------------------------------------
# UHD Driver Installation on Ubuntu 20.04 LTS
## Ettus Research Official Repository

To install UHD drivers, run the following commands:
- sudo add-apt-repository ppa:ettusresearch/uhd
- sudo apt-get update
- sudo apt-get install libuhd-dev uhd-host

## Download UHD Firmware Images
Download the required UHD firmware images with the following command:
- sudo /usr/lib/uhd/utils/uhd_images_downloader.py

## UHD Tools and Utilities
Commands Overview:
- uhd_find_devices: Detects connected UHD devices.
- uhd_fft -f 100M -s40M: A simple spectrum analyzer tool using a connected UHD device.
- uhd_rx_cfile: Records an I/Q sample stream to a file for later offline analysis.
- uhd_rx_nogui: Receives and plays incoming signals on your audio device (demodulates AM and FM signals).
- uhd_siggen_gui: A basic signal generator capable of creating common signals (e.g., sine, sweep, square, noise).
- gr_plot*: A suite of tools to display pre-recorded samples, including spectra, power spectral density (PSD), and time-domain representations.
