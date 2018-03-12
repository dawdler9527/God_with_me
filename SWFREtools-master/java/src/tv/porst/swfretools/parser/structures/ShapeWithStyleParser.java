package tv.porst.swfretools.parser.structures;

import static tv.porst.swfretools.parser.SWFParserHelpers.parseUBits;

import java.util.ArrayList;
import java.util.List;

import tv.porst.splib.binaryparser.UBits;
import tv.porst.swfretools.parser.SWFBinaryParser;
import tv.porst.swfretools.parser.SWFParserException;

/**
 * Parses ShapeWithStyle structures.
 * 
 * @author sp
 *
 */
public final class ShapeWithStyleParser {

	/**
	 * Parses a ShapeWithStyle structure.
	 * 
	 * @param parser The parser that parses the structure.
	 * @param fieldName The name of the structure in the parent structure.
	 * 
	 * @return The parsed structure.
	 * 
	 * @throws SWFParserException Thrown if the structure could not be parsed.
	 */
	public static ShapeWithStyle parse(final SWFBinaryParser parser, final String fieldName) throws SWFParserException {

		final FillStyleArray fillStyles = FillStyleArrayParser.parse(parser, fieldName + "::FillStyles");
		final LineStyleArray lineStyles = LineStyleArrayParser.parse(parser, fieldName + "::LineStyle");
		final UBits numFillBits = parseUBits(parser, 4, 0x00006, fieldName + "::NumFillBits");
		final UBits numLineBits = parseUBits(parser, 4, 0x00006, fieldName + "::NumLineBits");

		final List<ShapeRecord> shapeRecords = new ArrayList<ShapeRecord>();

		ShapeRecord shapeRecord = null;

		UBits currentNumFillBits = numFillBits;
		UBits currentNumLineBits = numLineBits;

		do {

			shapeRecord = ShapeRecordParser.parse(parser, currentNumFillBits, currentNumLineBits, fieldName + "::ShapeRecord");

			shapeRecords.add(shapeRecord);

			if (shapeRecord instanceof StyleChangeRecord) {

				if (((StyleChangeRecord) shapeRecord).getNumFillBits() != null) {
					currentNumFillBits = ((StyleChangeRecord) shapeRecord).getNumFillBits();
				}

				if (((StyleChangeRecord) shapeRecord).getNumLineBits() != null) {
					currentNumLineBits = ((StyleChangeRecord) shapeRecord).getNumLineBits();
				}
			}

		} while (!(shapeRecord instanceof EndShapeRecord));

		parser.align();

		return new ShapeWithStyle(fillStyles, lineStyles, numFillBits, numLineBits, shapeRecord);
	}
}