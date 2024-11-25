#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FM Modulation
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Basic_FM_Tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM Modulation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM Modulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Basic_FM_Tx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.vol = vol = -25
        self.samp_rate = samp_rate = 48000
        self.Gain = Gain = 10
        self.Fre = Fre = 103.424e6
        self.Dev = Dev = 100e3

        ##################################################
        # Blocks
        ##################################################
        self._Gain_range = Range(1, 79, 1, 10, 200)
        self._Gain_win = RangeWidget(self._Gain_range, self.set_Gain, "'Gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_win)
        self._Fre_range = Range(88e6, 107.9e6, 1000, 103.424e6, 200)
        self._Fre_win = RangeWidget(self._Fre_range, self.set_Fre, "'Fre'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Fre_win)
        self._Dev_range = Range(10e3, 100e3, 1, 100e3, 200)
        self._Dev_win = RangeWidget(self._Dev_range, self.set_Dev, "'Dev'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Dev_win)
        self._vol_range = Range(-30, -5, 0.5, -25, 200)
        self._vol_win = RangeWidget(self._vol_range, self.set_vol, "'vol'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._vol_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_samp_rate(250000)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_0.set_center_freq(Fre, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_gain(Gain, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=250,
                decimation=48,
                taps=[],
                fractional_bw=0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            Fre, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/david/Documentos-gnuradio/TX-RX-FM/Motorcycle driver.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=250000,
        	quad_rate=250000,
        	tau=75e-6,
        	max_dev=Dev,
        	fh=-1.0,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.analog_wfm_tx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_tx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Basic_FM_Tx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.Fre, self.samp_rate)

    def get_Gain(self):
        return self.Gain

    def set_Gain(self, Gain):
        self.Gain = Gain
        self.uhd_usrp_sink_0.set_gain(self.Gain, 0)

    def get_Fre(self):
        return self.Fre

    def set_Fre(self, Fre):
        self.Fre = Fre
        self.qtgui_sink_x_0.set_frequency_range(self.Fre, self.samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(self.Fre, 0)

    def get_Dev(self):
        return self.Dev

    def set_Dev(self, Dev):
        self.Dev = Dev




def main(top_block_cls=Basic_FM_Tx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
