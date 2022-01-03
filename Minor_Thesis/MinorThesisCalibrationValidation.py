import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import ticker
from matplotlib import rcParams
from datetime import timedelta
import numpy as np
from matplotlib.gridspec import GridSpec


class BrokenAxes:
    def __init__(
        self,
        xlims=None,
        ylims=None,
        d=0.015,
        tilt=45,
        subplot_spec=None,
        fig=None,
        despine=True,
        xscale=None,
        yscale=None,
        diag_color="k",
        height_ratios=None,
        width_ratios=None,
        *args,
        **kwargs
    ):
        """Creates a grid of axes that act like a single broken axes

        Parameters
        ----------
        xlims, ylims: (optional) None or tuple of tuples, len 2
            Define the ranges over which to plot. If `None`, the axis is left
            unsplit.
        d: (optional) double
            Length of diagonal split mark used to indicate broken axes
        tilt: (optional) double
            Angle of diagonal split mark
        subplot_spec: (optional) None or Gridspec.subplot_spec
            Defines a subplot
        fig: (optional) None or Figure
            If no figure is defined, `plt.gcf()` is used
        despine: (optional) bool
            Get rid of right and top spines. Default: True
        wspace, hspace: (optional) bool
            Change the size of the horizontal or vertical gaps
        xscale, yscale: (optional) None | str
            None: linear axis (default), 'log': log axis
        diag_color: (optional)
            color of diagonal lines
        {width, height}_ratios: (optional) | list of int
            The width/height ratios of the axes, passed to gridspec.GridSpec.
            By default, adapt the axes for a 1:1 scale given the ylims/xlims.
        hspace: float
            Height space between axes (NOTE: not horizontal space)
        wspace: float
            Widgth space between axes
        args, kwargs: (optional)
            Passed to gridspec.GridSpec

        Notes
        -----
        The broken axes effect is achieved by creating a number of smaller axes
        and setting their position and data ranges. A "big_ax" is used for
        methods that need the position of the entire broken axes object, e.g.
        `set_xlabel`.
        """

        self.diag_color = diag_color
        self.despine = despine
        self.d = d
        self.tilt = tilt

        if fig is None:
            self.fig = plt.gcf()
        else:
            self.fig = fig

        if width_ratios is None:
            if xlims:
                # Check if the user has asked for a log scale on x axis
                if xscale == "log":
                    width_ratios = [np.log(i[1]) - np.log(i[0]) for i in xlims]
                else:
                    width_ratios = [i[1] - i[0] for i in xlims]
            else:
                width_ratios = [1]

            # handle datetime xlims
            if isinstance(width_ratios[0], timedelta):
                width_ratios = [tt.total_seconds() for tt in width_ratios]

        if height_ratios is None:
            if ylims:
                # Check if the user has asked for a log scale on y axis
                if yscale == "log":
                    height_ratios = [np.log(i[1]) - np.log(i[0]) for i in ylims[::-1]]
                else:
                    height_ratios = [i[1] - i[0] for i in ylims[::-1]]
            else:
                height_ratios = [1]

            # handle datetime ylims
            if isinstance(height_ratios[0], timedelta):
                width_ratios = [tt.total_seconds() for tt in height_ratios]

        ncols, nrows = len(width_ratios), len(height_ratios)

        kwargs.update(
            ncols=ncols,
            nrows=nrows,
            height_ratios=height_ratios,
            width_ratios=width_ratios,
        )
        if subplot_spec:
            gs = gridspec.GridSpecFromSubplotSpec(
                subplot_spec=subplot_spec, *args, **kwargs
            )
            self.big_ax = plt.Subplot(self.fig, subplot_spec)
        else:
            gs = gridspec.GridSpec(*args, **kwargs)
            self.big_ax = plt.Subplot(self.fig, gridspec.GridSpec(1, 1)[0])

        [sp.set_visible(False) for sp in self.big_ax.spines.values()]
        self.big_ax.set_xticks([])
        self.big_ax.set_yticks([])
        self.big_ax.patch.set_facecolor("none")

        self.axs = []
        for igs in gs:
            ax = plt.Subplot(self.fig, igs)
            self.fig.add_subplot(ax)
            self.axs.append(ax)
        self.fig.add_subplot(self.big_ax)

        # get last axs row and first col
        self.last_row = []
        self.first_col = []
        for ax in self.axs:
            if ax.get_subplotspec().is_last_row():
                self.last_row.append(ax)
            if ax.get_subplotspec().is_first_col():
                self.first_col.append(ax)

        # Set common x/y lim for ax in the same col/row
        # and share x and y between them
        for i, ax in enumerate(self.axs):
            if ylims is not None:
                ax.set_ylim(ylims[::-1][i // ncols])
                ax.get_shared_y_axes().join(ax, self.first_col[i // ncols])
            if xlims is not None:
                ax.set_xlim(xlims[i % ncols])
                ax.get_shared_x_axes().join(ax, self.last_row[i % ncols])
        self.standardize_ticks()
        if d:
            self.draw_diags()
        self.set_spines()

    @staticmethod
    def draw_diag(ax, xpos, xlen, ypos, ylen, **kwargs):
        return ax.plot((xpos - xlen, xpos + xlen), (ypos - ylen, ypos + ylen), **kwargs)

    def draw_diags(self):
        """

        Parameters
        ----------
        d: float
            Length of diagonal split mark used to indicate broken axes
        tilt: float
            Angle of diagonal split mark
        """
        size = self.fig.get_size_inches()
        ylen = self.d * np.sin(self.tilt * np.pi / 180) * size[0] / size[1]
        xlen = self.d * np.cos(self.tilt * np.pi / 180)
        d_kwargs = dict(
            transform=self.fig.transFigure,
            color=self.diag_color,
            clip_on=False,
            lw=rcParams["axes.linewidth"],
        )

        ds = []
        for ax in self.axs:
            bounds = ax.get_position().bounds

            if ax.get_subplotspec().is_last_row():
                ypos = bounds[1]
                if not ax.get_subplotspec().is_last_col():
                    xpos = bounds[0] + bounds[2]
                    ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)
                if not ax.get_subplotspec().is_first_col():
                    xpos = bounds[0]
                    ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)

            if ax.get_subplotspec().is_first_col():
                xpos = bounds[0]
                if not ax.get_subplotspec().is_first_row():
                    ypos = bounds[1] + bounds[3]
                    ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)
                if not ax.get_subplotspec().is_last_row():
                    ypos = bounds[1]
                    ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)

            if not self.despine:
                if ax.get_subplotspec().is_first_row():
                    ypos = bounds[1] + bounds[3]
                    if not ax.get_subplotspec().is_last_col():
                        xpos = bounds[0] + bounds[2]
                        ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)
                    if not ax.get_subplotspec().is_first_col():
                        xpos = bounds[0]
                        ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)

                if ax.get_subplotspec().is_last_col():
                    xpos = bounds[0] + bounds[2]
                    if not ax.get_subplotspec().is_first_row():
                        ypos = bounds[1] + bounds[3]
                        ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)
                    if not ax.get_subplotspec().is_last_row():
                        ypos = bounds[1]
                        ds += self.draw_diag(ax, xpos, xlen, ypos, ylen, **d_kwargs)
        self.diag_handles = ds

    def set_spines(self):
        """Removes the spines of internal axes that are not boarder spines."""
        for ax in self.axs:
            ax.xaxis.tick_bottom()
            ax.yaxis.tick_left()
            if not ax.get_subplotspec().is_last_row():
                ax.spines["bottom"].set_visible(False)
                plt.setp(ax.xaxis.get_minorticklabels(), visible=False)
                plt.setp(ax.xaxis.get_minorticklines(), visible=False)
                plt.setp(ax.xaxis.get_majorticklabels(), visible=False)
                plt.setp(ax.xaxis.get_majorticklines(), visible=False)
            if self.despine or not ax.get_subplotspec().is_first_row():
                ax.spines["top"].set_visible(False)
            if not ax.get_subplotspec().is_first_col():
                ax.spines["left"].set_visible(False)
                plt.setp(ax.yaxis.get_minorticklabels(), visible=False)
                plt.setp(ax.yaxis.get_minorticklines(), visible=False)
                plt.setp(ax.yaxis.get_majorticklabels(), visible=False)
                plt.setp(ax.yaxis.get_majorticklines(), visible=False)
            if self.despine or not ax.get_subplotspec().is_last_col():
                ax.spines["right"].set_visible(False)

    def standardize_ticks(self, xbase=None, ybase=None):
        """Make all of the internal axes share tick bases

        Parameters
        ----------
        xbase, ybase: (optional) None or float
            If `xbase` or `ybase` is a float, manually set all tick locators to
            this base. Otherwise, use the largest base across internal subplots
            for that axis.
        """
        if xbase is None:
            if self.axs[0].xaxis.get_scale() == "log":
                xbase = max(
                    ax.xaxis.get_ticklocs()[1] / ax.xaxis.get_ticklocs()[0]
                    for ax in self.axs
                    if ax.get_subplotspec().is_last_row()
                )
            else:
                xbase = max(
                    ax.xaxis.get_ticklocs()[1] - ax.xaxis.get_ticklocs()[0]
                    for ax in self.axs
                    if ax.get_subplotspec().is_last_row()
                )
        if ybase is None:
            if self.axs[0].yaxis.get_scale() == "log":
                ybase = max(
                    ax.yaxis.get_ticklocs()[1] / ax.yaxis.get_ticklocs()[0]
                    for ax in self.axs
                    if ax.get_subplotspec().is_first_col()
                )
            else:
                ybase = max(
                    ax.yaxis.get_ticklocs()[1] - ax.yaxis.get_ticklocs()[0]
                    for ax in self.axs
                    if ax.get_subplotspec().is_first_col()
                )

        for ax in self.axs:
            if ax.get_subplotspec().is_first_col():
                if ax.yaxis.get_scale() == "log":
                    ax.yaxis.set_major_locator(ticker.LogLocator(ybase))
                else:
                    ax.yaxis.set_major_locator(ticker.MultipleLocator(ybase))
            if ax.get_subplotspec().is_last_row():
                if ax.xaxis.get_scale() == "log":
                    ax.xaxis.set_major_locator(ticker.LogLocator(xbase))
                else:
                    ax.xaxis.set_major_locator(ticker.MultipleLocator(xbase))

    def __getattr__(self, method):
        """Catch all methods that are not defined and pass to internal axes
        (e.g. plot, errorbar, etc.).
        """
        return CallCurator(method, self)

    def subax_call(self, method, args, kwargs):
        """Apply method call to all internal axes. Called by CallCurator."""
        result = []
        for ax in self.axs:
            if ax.xaxis.get_scale() == "log":
                ax.xaxis.set_major_locator(ticker.LogLocator())
            else:
                ax.xaxis.set_major_locator(ticker.AutoLocator())
            if ax.yaxis.get_scale() == "log":
                ax.yaxis.set_major_locator(ticker.LogLocator())
            else:
                ax.yaxis.set_major_locator(ticker.AutoLocator())
            result.append(getattr(ax, method)(*args, **kwargs))

        self.standardize_ticks()
        self.set_spines()

        return result

    def set_xlabel(self, label, labelpad=15, **kwargs):
        return self.big_ax.set_xlabel(label, labelpad=labelpad, **kwargs)

    def set_ylabel(self, label, labelpad=30, **kwargs):
        return self.big_ax.set_ylabel(label, labelpad=labelpad, **kwargs)

    def set_title(self, *args, **kwargs):
        return self.big_ax.set_title(*args, **kwargs)

    def legend(self, handles=None, labels=None, *args, **kwargs):
        if handles is None or labels is None:
            h, l = self.axs[0].get_legend_handles_labels()
            if handles is None:
                handles = h
            if labels is None:
                labels = l
        return self.big_ax.legend(handles, labels, *args, **kwargs)

    def axis(self, *args, **kwargs):
        [ax.axis(*args, **kwargs) for ax in self.axs]

    def secondary_yaxis(self, functions=None, label=None, labelpad=30):
        [
            ax.secondary_yaxis("right", functions=functions)
            for ax in self.axs
            if ax.get_subplotspec().is_last_col()
        ]
        secax = self.big_ax.secondary_yaxis("right", functions=functions)

        secax.spines["right"].set_visible(False)
        secax.set_yticks([])
        secax.patch.set_facecolor("none")

        if label is not None:
            secax.set_ylabel(label, labelpad=labelpad)

        return secax

    def secondary_xaxis(self, functions=None, label=None, labelpad=30):
        [
            ax.secondary_xaxis("top", functions=functions)
            for ax in self.axs
            if ax.get_subplotspec().is_first_row()
        ]
        secax = self.big_ax.secondary_xaxis("top", functions=functions)

        secax.spines["top"].set_visible(False)
        secax.set_xticks([])
        secax.patch.set_facecolor("none")

        if label is not None:
            secax.set_xlabel(label, labelpad=labelpad)

        return secax

    def text(self, x, y, s, *args, **kwargs):
        # find axes that contains text
        for ax in self.axs:
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()
            if xlim[0] < x < xlim[1] and ylim[0] < y < ylim[1]:
                ax.text(x, y, s, *args, **kwargs)
                return

        raise ValueError('(x,y) coordinate of text not within any axes')


class CallCurator:
    """Used by BrokenAxes.__getattr__ to pass methods to internal axes."""

    def __init__(self, method, broken_axes):
        self.method = method
        self.broken_axes = broken_axes

    def __call__(self, *args, **kwargs):
        return self.broken_axes.subax_call(self.method, args, kwargs)

    def get_yaxis(self, *args, **kwargs):
        return self.broken_axes.big_ax.get_yaxis(*args, **kwargs)

    def get_shared_x_axes(self, *args, **kwargs):
        return self.broken_axes.big_ax.get_shared_x_axes(*args, **kwargs)

    def plot(self, *args, **kwargs):
        return self.broken_axes.plot(*args, **kwargs)

    def get_lines(self, *args, **kwargs):
        return self.broken_axes.get_lines(*args, **kwargs)

    def secondary_yaxis(self, *args, **kwargs):
        return self.broken_axes.secondary_yaxis(*args, **kwargs)

    def secondary_xaxis(self, *args, **kwargs):
        return self.broken_axes.secondary_xaxis(*args, **kwargs)


def brokenaxes(*args, **kwargs):
    """Convenience method for `BrokenAxes` class.

    Parameters
    ----------
    args, kwargs: passed to `BrokenAxes()`

    Returns
    -------
    out: `BrokenAxes`
    """
    return BrokenAxes(*args, **kwargs)


df1 = pd.read_csv('E:\\MinorThesisVS\\see-me-percentage-0per.txt.txt', sep=" ", header = None)

print(df1)


df_60 = df1[(df1[6] > 55) & (df1[6] < 65)]
df_80 = df1[(df1[6] > 75) & (df1[6] < 85)]
df_100 = df1[(df1[6] > 95) & (df1[6] < 105)]
df_120 = df1[(df1[6] > 115) & (df1[6] < 125)]
df_140 = df1[(df1[6] > 135) & (df1[6] < 145)]

# 60
weight_vt_60 = df_60[0].mean()
fuel_vt_60 = df_60[1].mean()
time_vt_60 = df_60[2].mean()

weight_avg_60 = df_60[3].mean()
fuel_avg_60 = df_60[4].mean()
time_avg_60 = df_60[5].mean()

weight_d_60 = df_60[6].mean()
fuel_d_60 = df_60[7].mean()
time_d_60 = df_60[8].mean()

weight_lt_60 = df_60[9].mean()
fuel_lt_60 = df_60[10].mean()
time_lt_60 = df_60[11].mean()

# 80
weight_vt_80 = df_80[0].mean()
fuel_vt_80 = df_80[1].mean()
time_vt_80 = df_80[2].mean()

weight_avg_80 = df_80[3].mean()
fuel_avg_80 = df_80[4].mean()
time_avg_80 = df_80[5].mean()

weight_d_80 = df_80[6].mean()
fuel_d_80 = df_80[7].mean()
time_d_80 = df_80[8].mean()

weight_lt_80 = df_80[9].mean()
fuel_lt_80 = df_80[10].mean()
time_lt_80 = df_80[11].mean()

# 100
weight_vt_100 = df_100[0].mean()
fuel_vt_100 = df_100[1].mean()
time_vt_100 = df_100[2].mean()

weight_avg_100 = df_100[3].mean()
fuel_avg_100 = df_100[4].mean()
time_avg_100 = df_100[5].mean()

weight_d_100 = df_100[6].mean()
fuel_d_100 = df_100[7].mean()
time_d_100 = df_100[8].mean()

weight_lt_100 = df_100[9].mean()
fuel_lt_100 = df_100[10].mean()
time_lt_100 = df_100[11].mean()

# 120
weight_vt_120 = df_120[0].mean()
fuel_vt_120 = df_120[1].mean()
time_vt_120 = df_120[2].mean()

weight_avg_120 = df_120[3].mean()
fuel_avg_120 = df_120[4].mean()
time_avg_120 = df_120[5].mean()

weight_d_120 = df_120[6].mean()
fuel_d_120 = df_120[7].mean()
time_d_120 = df_120[8].mean()

weight_lt_120 = df_120[9].mean()
fuel_lt_120 = df_120[10].mean()
time_lt_120 = df_120[11].mean()

# 140
weight_vt_140 = df_140[0].mean()
fuel_vt_140 = df_140[1].mean()
time_vt_140 = df_140[2].mean()

weight_avg_140 = df_140[3].mean()
fuel_avg_140 = df_140[4].mean()
time_avg_140 = df_140[5].mean()

weight_d_140 = df_140[6].mean()
fuel_d_140 = df_140[7].mean()
time_d_140 = df_140[8].mean()

weight_lt_140 = df_140[9].mean()
fuel_lt_140 = df_140[10].mean()
time_lt_140 = df_140[11].mean()

x_axis = [60, 80, 100, 120, 140]
y1 = [fuel_vt_60,fuel_vt_80,fuel_vt_100,fuel_vt_120,fuel_vt_140]
y2 = [fuel_avg_60,fuel_avg_80,fuel_avg_100,fuel_avg_120,fuel_avg_140]
y3 = [fuel_d_60,fuel_d_80,fuel_d_100,fuel_d_120,fuel_d_140]
y4 = [fuel_lt_60,fuel_lt_80,fuel_lt_100,fuel_lt_120,fuel_lt_140]

# y1 = [weight_vt_60,weight_vt_80,weight_vt_100,weight_vt_120,weight_vt_140]
# y2 = [weight_avg_60,weight_avg_80,weight_avg_100,weight_avg_120,weight_avg_140]
# y3 = [weight_d_60,weight_d_80,weight_d_100,weight_d_120,weight_d_140]
# y4 = [weight_lt_60,weight_lt_80,weight_lt_100,weight_lt_120,weight_lt_140]

# y1 = [time_vt_60,time_vt_80,time_vt_100,time_vt_120,time_vt_140]
# y2 = [time_avg_60,time_avg_80,time_avg_100,time_avg_120,time_avg_140]
# y3 = [time_d_60,time_d_80,time_d_100,time_d_120,time_d_140]
# y4 = [time_lt_60,time_lt_80,time_lt_100,time_lt_120,time_lt_140]


# plt.plot(x_axis, y1, marker='o', label="VT-CPFM Model")
# plt.plot(x_axis, y2, marker='o', label="Mesoscopic Model")
# plt.plot(x_axis, y3, marker='o', label="Dijkstra Routing Model")
# plt.plot(x_axis, y4, marker='o', label="Lowest Time Model")
# plt.xticks(x_axis)
# plt.xlabel("Traffic Signal Circle Time (S)")
# plt.ylabel("Travel Distance (KM)")
# plt.legend()
#
# plt.plot(x_axis, y2)
# plt.title("The Comparison of Travel Time according to Traffic Signal Circle Time")
# plt.show()



# bax = brokenaxes(ylims=((0,1),(50,170)), hspace=0.5, despine=False)
# bax.plot(x_axis, y1, marker='o', label = 'VT Model')
# bax.plot(x_axis, y2, marker='o', label = 'Mesoscopic Model')
# bax.plot(x_axis, y3, marker='o', label = 'Dijkstra Model')
# bax.plot(x_axis, y4, marker='o', label = 'Lowest Time Model')
# bax.set_xticks(x_axis)
# bax.set_title('Travel Distance Comparison for Case 2(20% Traffic Signal)')
# bax.legend(loc=2)
# bax.set_xlabel('Shortest Distance (KM)')
# bax.set_ylabel('Travel Distance (KM)')
# plt.show()

sps1,sps2 = GridSpec(1,2)
bax = brokenaxes(ylims=((0,1),(5500,13000)), hspace=0.5, despine=False, subplot_spec=sps1)
bax.plot(x_axis, y1, marker='o', label = 'VT Model')
bax.plot(x_axis, y2, marker='o', label = 'Mesoscopic Model')
bax.plot(x_axis, y3, marker='o', label = 'Dijkstra Model')
bax.plot(x_axis, y4, marker='o', label = 'Lowest Time Model')
bax.set_xticks(x_axis)
bax.set_title('Travel Time Comparison for Case 2 (0% Traffic Signal)')
bax.legend(loc=2)
bax.set_xlabel('Travel Distance (KM)')
bax.set_ylabel('Travel Time (S)')


bax = brokenaxes(ylims=((0,0.01),(3,9)), hspace=0.5, despine=False, subplot_spec=sps2)
bax.plot(x_axis, y1, marker='o', label = 'VT Model')
bax.plot(x_axis, y2, marker='o', label = 'Mesoscopic Model')
bax.plot(x_axis, y3, marker='o', label = 'Dijkstra Model')
bax.plot(x_axis, y4, marker='o', label = 'Lowest Time Model')
bax.set_xticks(x_axis)
bax.set_title('Fuel Consumption Comparison (70% Traffic Signal)')
bax.legend(loc=2)
bax.set_xlabel('Travel Distance (KM)')
bax.set_ylabel('Fuel Consumption (L)')
plt.show()

















