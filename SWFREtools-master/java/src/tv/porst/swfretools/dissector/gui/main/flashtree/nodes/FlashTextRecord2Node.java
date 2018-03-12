package tv.porst.swfretools.dissector.gui.main.flashtree.nodes;

import tv.porst.swfretools.parser.structures.TextRecord2;

/**
 * Node that represents a TextRecord object in the Flash tree.
 */
public final class FlashTextRecord2Node extends FlashTreeNode<TextRecord2> {

	/**
	 * Creates a new node object
	 * 
	 * @param name Name of the node.
	 * @param value Flash structure represented by the node.
	 */
	public FlashTextRecord2Node(final String name, final TextRecord2 value) {
		super(name, value);

		createChildren();
	}

	/**
	 * Creates the child nodes of the node.
	 */
	private void createChildren() {
		addNode("TextRecordType", getUserObject().getTextRecordType());
		addNode("StyleFlagsReserved", getUserObject().getStyleFlagsReserved());
		addNode("StyleFlagsHasFont", getUserObject().getStyleFlagsHasFont());
		addNode("StyleFlagsHasColor", getUserObject().getStyleFlagsHasColor());
		addNode("StyleFlagsHasYOffset", getUserObject().getStyleFlagsHasYOffset());
		addNode("StyleFlagsHasXOffset", getUserObject().getStyleFlagsHasXOffset());
		addNode("FontID", getUserObject().getFontId());
		addNode("TextColor", getUserObject().getTextColor());
		addNode("XOffset", getUserObject().getxOffset());
		addNode("YOffset", getUserObject().getyOffset());
		addNode("TextHeight", getUserObject().getTextHeight());
		addNode("GlyphCount", getUserObject().getGlyphCount());
		addNode("GlyphEntries", getUserObject().getGlyphEntries());
	}

	@Override
	public String toString() {
		return String.format("%s : TEXTRECORD", getName());
	}
}