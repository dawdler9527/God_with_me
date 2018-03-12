package tv.porst.swfretools.parser.structures;

import tv.porst.splib.binaryparser.IFileElement;
import tv.porst.splib.binaryparser.UINT16;
import tv.porst.swfretools.parser.SWFParserHelpers;

/**
 * Represents a LineStyle structure.
 * 
 * @author sp
 *
 */
public final class LineStyle implements IFileElement {

	/**
	 * Width of line in twips.
	 */
	private final UINT16 width;

	/**
	 * Color value including alpha channel.
	 */
	private final RGB color;

	/**
	 * Creates a new LineStyle object.
	 * 
	 * @param width Width of line in twips.
	 * @param color Color value including alpha channel.
	 */
	public LineStyle(final UINT16 width, final RGB color) {

		this.width = width;
		this.color = color;
	}

	@Override
	public int getBitLength() {
		return SWFParserHelpers.addBitLengths(width, color);
	}

	@Override
	public int getBitPosition() {
		return width.getBitPosition();
	}

	/**
	 * Returns the color value including alpha channel.
	 *
	 * @return The color value including alpha channel.
	 */
	public RGB getColor() {
		return color;
	}

	/**
	 * Returns the width of line in twips.
	 *
	 * @return The width of line in twips.
	 */
	public UINT16 getWidth() {
		return width;
	}
}